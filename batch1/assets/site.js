document.documentElement.classList.add('js');
const toggle=document.querySelector('.menu-toggle');
const nav=document.querySelector('.primary-nav');
if(toggle&&nav){
  toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?'Schliessen':'Menü';});
  nav.addEventListener('click',event=>{if(event.target.closest('a')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menü';}});
  document.addEventListener('keydown',event=>{if(event.key==='Escape'&&nav.classList.contains('open')){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent='Menü';toggle.focus();}});
}
const form=document.querySelector('#contact-form');
if(form){form.addEventListener('submit',event=>{event.preventDefault();const data=new FormData(form);const name=String(data.get('name')||'').trim();const topic=String(data.get('topic')||'').trim();const message=String(data.get('message')||'').trim();const body=`Name: ${name}\nAnliegen: ${topic}\n\n${message}`;window.location.href=`mailto:david@jakoda.ch?subject=${encodeURIComponent(topic||'IT-Anfrage')}&body=${encodeURIComponent(body)}`;});}
