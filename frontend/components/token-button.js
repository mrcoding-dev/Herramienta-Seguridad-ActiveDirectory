import React, { useState } from 'react';
import PropTypes from 'prop-types';
import { Notify } from 'notiflix/build/notiflix-notify-aio';

const TokenButton = (props) => {
  const [inputOpen, setInputOpen] = useState(false);
  const [token, setToken] = useState('');

  const toggleInput = () => {
    setInputOpen(!inputOpen);
  };

  const handleTokenChange = (event) => {
    setToken(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Enviar petición POST a la API
    fetch('http://127.0.0.1:8000/agregar-token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ message:token })
    })
      .then(response => {
        console.log(response)
        // Manejar la respuesta de la API
        response.json().then(jsonResponse => {
          //Notify.success(jsonResponse.message);
          Notify.success("Token JWT agregado");
        });
        setToken('');
        setInputOpen(false);
      })
      .catch(error => {
        console.log(error)
        // Manejar errores
        if (error.response) {
          Notify.failure(error.response.data.detail);
        }
      });
  };

  return (
    <>
      <div className="token-button-container">
        {inputOpen ? (
          <form onSubmit={handleSubmit} className="token-button-form">
            <input
              type="text"
              placeholder="Ingrese su token aquí"
              value={token}
              onChange={handleTokenChange}
              className="token-button-input"
            />
            <div className="token-button-actions">
              <button type="submit" className="token-button-submit">
                Agregar
              </button>
              <button type="button" onClick={toggleInput} className="token-button-close">
                X
              </button>
            </div>
          </form>
        ) : (
          <div className="token-button" onClick={toggleInput}>
            <span className="token-button-text">{props.token}</span>
          </div>
        )}
      </div>
      <style jsx>
        {`
          .token-button-container {
            position: relative;
            display: inline-block;
            background-color: transparent;
          }
          .token-button {
            cursor: pointer;
            background-color: #246fe0;
            border-radius: 4px;
            padding: 4px 8px;
            color: #fff;
            font-size: 14px;
          }
          .token-button-form {
            position: absolute;
            top: 100%;
            left: 0;
            width: 200px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.16);
            padding: 8px;
            z-index: 10;
          }
          .token-button-input {
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 4px 8px;
            margin-bottom: 4px;
            width: 100%;
          }
          .token-button-actions {
            display: flex;
            justify-content: space-between;
            align-items: center;
          }
          .token-button-submit {
            background-color: #246fe0;
            border: none;
            border-radius: 4px;
            color: #fff;
            padding: 4px 8px;
            cursor: pointer;
          }
          .token-button-close {
            background-color: #ccc;
            border: none;
            border-radius: 50%;
            color: #fff;
            cursor: pointer;
            display: flex;
            justify-content: center;
            align-items: center;
            width: 20px;
            height: 20px;
            .token-button-text {
              color: #ffffff;
              font-size: 10px;
            }
          `}
        </style>
      </>
    );
};

TokenButton.defaultProps = {
  token: 'Agregar Token',
};

TokenButton.propTypes = {
  token: PropTypes.string,
};

export default TokenButton;

            