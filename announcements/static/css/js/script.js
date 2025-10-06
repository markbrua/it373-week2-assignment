document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.read-more-toggle');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const li = button.closest('.announcement');
            const shortContent = li.querySelector('.content-short');
            const fullContent = li.querySelector('.content-full');

            if (fullContent.style.display === 'none' || fullContent.style.display === '') {
                fullContent.style.display = 'block';
                shortContent.style.display = 'none';
                button.textContent = 'Show less';
            } else {
                fullContent.style.display = 'none';
                shortContent.style.display = 'block';
                button.textContent = 'Read more';
            }
        });
    });
});
