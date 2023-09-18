<style>:root {
    --header_color: #b5b5b5;
    --module_color: #c6c96d;
}
h {
    color: var(--header_color);
}

.module{
color: var(--module_color); 
font-family: 'Courier', monospace; 
font-size: 18px;
}
</style>

<h3>Модули форм</h3>
<hr>
<h5>
    Модуль: 
    <span class="module">
        form_reg_log
    </span>
</h5>
Класс формы аутентификации

| LogiInForm |
|------------|
| user_login |
| user_pass  |
| submit_log |     
| user_save  |

<br>
Класс формы восстановления пароля

| PasswordRecovery |
|------------------|
| user_login       |
| submit           |

<br>
Класс формы регистрации

| RegistrationForm |
|------------------|
| user_login       |
| user_pass        |
| user_conf_pass   |
| user_save        |
| submit_reg       |

<hr>
<h5>
    Модуль: 
    <span class="module">
        forms_of_platform_interaction
    </span>
</h5>
Класс формы обратной связи

| FeedbackForm    |
|-----------------|
| user_first_name |
| user_last_name  |
| user_login      |
| user_message    |
| submit_int      |

<hr>