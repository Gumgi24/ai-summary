document.addEventListener('DOMContentLoaded', function() {
    // Fermer les messages flash
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(function(message) {
        const closeBtn = message.querySelector('.close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', function() {
                message.style.opacity = '0';
                setTimeout(function() {
                    message.remove();
                }, 300);
            });
        }
        
        // Auto-masquer après 5 secondes
        setTimeout(function() {
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 300);
        }, 5000);
    });
    
    // Animation des boutons
    const buttons = document.querySelectorAll('button, .action-btn');
    buttons.forEach(function(button) {
        button.addEventListener('mousedown', function() {
            this.style.transform = 'scale(0.98)';
        });
        
        button.addEventListener('mouseup', function() {
            this.style.transform = '';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = '';
        });
    });
    
    // Effet hover sur les étapes
    const steps = document.querySelectorAll('.step');
    steps.forEach(function(step) {
        step.addEventListener('mouseenter', function() {
            const icon = this.querySelector('.step-icon');
            if (icon) {
                icon.style.transform = 'scale(1.1) rotate(5deg)';
            }
        });
        
        step.addEventListener('mouseleave', function() {
            const icon = this.querySelector('.step-icon');
            if (icon) {
                icon.style.transform = '';
            }
        });
    });
    
    // Animation lors du scroll pour les éléments de la page
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-step');
        
        elements.forEach(function(element) {
            const position = element.getBoundingClientRect();
            
            // Si l'élément est dans la vue
            if (position.top < window.innerHeight && position.bottom >= 0) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };
    
    // Déclencher l'animation au chargement
    animateOnScroll();
    
    // Déclencher l'animation lors du scroll
    window.addEventListener('scroll', animateOnScroll);
});
