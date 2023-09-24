const inputElements = [...document.querySelectorAll('input.code-input')]

inputElements.forEach((ele,index)=>{
  ele.addEventListener('keydown',(e)=>{
    // if the keycode is backspace & the current field is empty
    // focus the input before the current. Then the event happens
    // which will clear the "before" input box.
    if(e.keyCode === 8 && e.target.value==='') inputElements[Math.max(0,index-1)].focus()
  })
  ele.addEventListener('input',(e)=>{
    const [first,...rest] = e.target.value;
    e.target.value = first ?? '' // first will be undefined when backspace was entered, so set the input to ""
    const lastInputBox = index===inputElements.length-1
    const didInsertContent = first!==undefined
    if (didInsertContent) {
      if (!lastInputBox) {
        inputElements[index+1].focus()
        inputElements[index+1].value = rest.join('')
        inputElements[index+1].dispatchEvent(new Event('input'))
      } else {
        const code = inputElements.map(({value})=>value).join('')
        alert(code);
      }
    }
  })
})

function onSubmit(e){
  e.preventDefault()
  const code = inputElements.map(({value})=>value).join('')
  console.log(code)
}
