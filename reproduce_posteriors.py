#!/usr/bin/env python3
import argparse, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pta', required=True)
    ap.add_argument('--cmb', required=True)
    ap.add_argument('--lisa', required=True)
    ap.add_argument('--out', default='results')
    args = ap.parse_args()

    import os
    os.makedirs(args.out, exist_ok=True)

    # Load PTA
    df = pd.read_csv(args.pta)
    f = df['freq_Hz'].values
    y = df['log10rho_median'].values
    ylo = df['log10rho_p16'].values
    yhi = df['log10rho_p84'].values

    # PTA preview
    plt.figure()
    plt.xscale('log')
    plt.plot(f, y, marker='o', linestyle='None')
    plt.fill_between(f, ylo, yhi, alpha=0.2)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('log10 rho (demo units)')
    plt.title('PTA spectrum (quick-look)')
    plt.savefig(f"{args.out}/PTA_preview.png", dpi=200, bbox_inches='tight')
    plt.close()

    # Load LISA
    lisa = pd.read_csv(args.lisa)
    lf = lisa['f_Hz'].values
    Sn = lisa['Sn_1_per_Hz'].values

    plt.figure()
    plt.xscale('log'); plt.yscale('log')
    plt.plot(lf, Sn)
    plt.xlabel('frequency [Hz]')
    plt.ylabel('S_n [1/Hz]')
    plt.title('LISA sensitivity (quick-look)')
    plt.savefig(f"{args.out}/LISA_preview.png", dpi=200, bbox_inches='tight')
    plt.close()

    # Save a tiny JSON combining priors
    with open(args.cmb) as fjson:
        cmb = json.load(fjson)
    with open(f"{args.out}/run_info.json", "w") as fout:
        json.dump({"pta_csv": args.pta, "lisa_csv": args.lisa, "cmb": cmb}, fout, indent=2)

if __name__ == "__main__":
    main()
