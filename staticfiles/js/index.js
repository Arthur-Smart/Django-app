const commentEl = document.querySelectorAll('.comments')
const commentBtn = document.getElementById('comment')


commentBtn.addEventListener('click', () => {
    commentEl.classList.add('toggle')
})
