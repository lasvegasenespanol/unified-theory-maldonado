
document.querySelectorAll('details').forEach(d=>{
  d.addEventListener('toggle', ()=>{
    if(d.open){ d.querySelector('summary').classList.add('open'); }
    else{ d.querySelector('summary').classList.remove('open'); }
  })
});
