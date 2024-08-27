from flask import Flask, render_template, request, redirect, url_for
from src.model.user import User
from src.dao.user_dao import UserDAO

def validate_inputs():
                try:
                    data = {
                        'nome': request.form.get('name_input'),
                        'ddd': request.form.get('ddd_input'),
                        'número_da_residência': request.form.get('number_residence_input'),
                        'bairro': request.form.get('district_input'),
                        'estado': request.form.get('state_input'),
                        'senha': request.form.get('password_input'),
                        'email': request.form.get('email_input'),
                        'telefone': request.form.get('phone_input'),
                        'rua': request.form.get('street_input'),
                        'cidade': request.form.get('city_input'),
                        'cep': request.form.get('cep_input'),
                        'confirmação_de_senha': request.form.get('conf_senha_input')
                    }
        
                    if None in data.values():
                        raise ValueError("One or more form inputs are missing")
                    
                    elif data['senha'] != data['confirmação_de_senha']:
                        raise ValueError("Passwords do not match")

                    else:
                        def insert_dao_data():
                            user_dao = UserDAO.build_user(data)
                            return UserDAO.insert_user(user_dao)
                    
                    return redirect(url_for('success'))
                
                except ValueError as e:
                    return redirect(url_for('error', error=str(e)))
                
                except Exception as e:
                    return redirect(url_for('error', error=str(e)))

    