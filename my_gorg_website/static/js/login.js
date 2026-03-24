document.addEventListener('DOMContentLoaded', function() {
    
    const firstName = document.getElementById('firstName');
    const lastName = document.getElementById('lastName');
    const age = document.getElementById('age');
    const email = document.getElementById('email');
    const album = document.getElementById('album');

    const firstNameHint = document.getElementById('firstNameHint');
    const lastNameHint = document.getElementById('lastNameHint');
    const ageHint = document.getElementById('ageHint');
    const emailHint = document.getElementById('emailHint');
    const resultDiv = document.getElementById('validationResult');

    function validateFirstName(value) {
        return /^[A-Z][a-z]+$/.test(value);
    }

    function validateLastName(value) {
        return /^[A-Z][a-z]+$/.test(value);
    }

    function validateAge(value) {
        let num = parseInt(value);
        return !isNaN(num) && num >= 18 && num <= 100;
    }

    
   function validateEmail(value) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value.trim());
    }
    
    function updateHint(input, hint, isValid, validMessage, errorMessage, emptyMessage) {
        if (input.value === '') {
            hint.style.color = '#888';
            hint.innerHTML = emptyMessage;
            input.style.borderColor = '#dbcfcf';
        } else if (isValid) {
            hint.style.color = '#4CAF50';
            hint.innerHTML = validMessage;
            input.style.borderColor = '#4CAF50';
        } else {
            hint.style.color = '#f44336';
            hint.innerHTML = errorMessage;
            input.style.borderColor = '#f44336';
        }
    }

    firstName.addEventListener('input', function(e) {
        updateHint(
            firstName, firstNameHint,
            validateFirstName(e.target.value),
            'правильно',
            'латиниица, с заглавной, только буквы',
            'латиница, с заглавной'
        );
    });

    lastName.addEventListener('input', function(e) {
        updateHint(
            lastName, lastNameHint,
            validateLastName(e.target.value),
            'правильно',
            'латиниица, с заглавной, только буквы',
            'латиница, с заглавной'
        );
    });

    age.addEventListener('input', function(e) {
        updateHint(
            age, ageHint,
            validateAge(e.target.value),
            'правильно',
            'от 18 до 100',
            'от 18 до 100'
        );
    });

    
    email.addEventListener('input', function(e) {

        updateHint(
            email, emailHint, validateEmail(e.target.value),
            'правильно',
            'name@domain.com',
            'формат: name@domain.com'
        );
    });

    window.validateForm = function(event) {
        event.preventDefault();

        let firstNameVal = firstName.value;
        let lastNameVal = lastName.value;
        let ageVal = age.value;
        let emailVal = email.value;

        let errors = [];
        let isValid = true;

        if (!validateFirstName(firstNameVal)) {
            errors.push('first name');
            isValid = false;
        }

        if (!validateLastName(lastNameVal)) {
            errors.push('last name');
            isValid = false;
        }

        if (!validateAge(ageVal)) {
            errors.push('age');
            isValid = false;
        }

        
        if (!validateEmail(emailVal)) {
            errors.push('email');
            isValid = false;
        }

        if (isValid) {
            
            // сброс формы
            firstName.value = '';
            lastName.value = '';
            age.value = '';
            email.value = '';
            album.value = '';
            
            updateHint(firstName, firstNameHint, false, '', '', 'латиница, с заглавной (Maria)');
            updateHint(lastName, lastNameHint, false, '', '', 'только буквы');
            updateHint(age, ageHint, false, '', '', 'от 18 до 100');
            updateHint(email, emailHint, false, '', '', 'формат: name@domain.com');
        } else {
            resultDiv.style.backgroundColor = '#fff0f0';
            resultDiv.style.color = '#f44336';
            resultDiv.innerHTML = 'ошибка в полях: ' + errors.join(', ');
        }

        return false;
    };

});