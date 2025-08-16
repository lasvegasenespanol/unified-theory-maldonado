// Minimal enhancements: smooth anchor scrolling & active link state
(function(){
  function smoothScroll(e){
    if(e.target.matches('a[href^="#"]')){
      const id = e.target.getAttribute('href');
      const el = document.querySelector(id);
      if(el){
        e.preventDefault();
        el.scrollIntoView({behavior:'smooth', block:'start'});
        history.pushState(null, '', id);
      }
    }
  }
  document.addEventListener('click', smoothScroll, false);

  // Active link on scroll
  const sections = Array.from(document.querySelectorAll('main section[id]'));
  const links = Array.from(document.querySelectorAll('.nav a'));
  function setActive(){
    let idx = 0;
    const y = window.scrollY + 120;
    for(let i=0;i<sections.length;i++){
      if(sections[i].offsetTop <= y) idx = i;
    }
    links.forEach(l => l.classList.remove('active'));
    const id = sections[idx]?.id;
    const active = document.querySelector('.nav a[href="#'+id+'"]');
    if(active) active.classList.add('active');
  }
  document.addEventListener('scroll', setActive, {passive:true});
  setActive();
})();