import React from 'react';
import Form from 'react-json-to-form';
import UserLogin from "hocs/auth/userLogin";


const Login = (props) => {
    const data = {
        allFieldsRequired: true,
        fieldClass: 'pz-form__field',
        fields: [
            {
                name: 'username',
                type: 'text',
                label: {
                    value: 'Username'
                }
            },
            {
                name: 'password',
                type: 'password',
                label: {
                    value: 'Password'
                }
            },
            {
                name: 'login',
                type: 'submit',
                value: 'Login',
                fieldClass: 'pz-form__field--button'
            }
        ]
    }

    const handleSubmit = (e, data) => {
        props.login(data);
    };

    return (
        <main className='pz-login grid-center-wh'>
            <Form
                data={data}
                onSubmit={handleSubmit}
                className='pz-form'
            >
                <h1 className='pz-form__title'>Login</h1>
                { props.errorMessage && <p className='pz-form__message'>{props.errorMessage}</p> }
            </Form>
        </main>
    );
};

export default UserLogin(Login);