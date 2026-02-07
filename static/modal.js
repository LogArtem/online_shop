document.addEventListener('DOMContentLoaded', function () {

    
    var modal = document.getElementById('product-modal');
    var modalImage = document.getElementById('modal-image');
    var modalDesc = document.getElementById('modal-desc');
    var modalMeta = document.getElementById('modal-meta');
    var modalClose = document.querySelector('.modal-close');

    
    function openModal() {
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
    }

    
    function closeModal() {
        modal.classList.remove('open');
        modal.setAttribute('aria-hidden', 'true');
    }

    modalClose.addEventListener('click', closeModal);

});

