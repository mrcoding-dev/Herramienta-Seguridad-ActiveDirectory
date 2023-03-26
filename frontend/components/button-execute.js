import React from 'react'
import PropTypes from 'prop-types'
import { confirmAlert } from 'react-confirm-alert'
import 'react-confirm-alert/src/react-confirm-alert.css'
import { Notify } from 'notiflix/build/notiflix-notify-aio'
import axios from 'axios';

function ejecutarDeuso() {
  axios.get('http://127.0.0.1:8000/desuso')
    .then(function(response) {
      // Mostrar mensaje de éxito con Notiflix
      const jsonResponse = response.data;
      Notify.success(jsonResponse.message);
    })
    .catch(function(error) {
      // Mostrar mensaje de error con Notiflix
      console.log(error)
      if (error.response) {
        Notify.failure(error.response.data.detail);
      } else {
        Notify.failure('Error al realizar la petición');
      }
    });
}

const ButtonExecute = (props) => {
  const { rootClassName, ejecutar, title, message, onYesClick, onNoClick } = props

  const handleClick = () => {
    confirmAlert({
      title,
      message,
      buttons: [
        {
          label: 'Yes',
          onClick: () => {
            onYesClick()
            ejecutarDeuso() 
          }
        },
        {
          label: 'No',
          onClick: onNoClick
        }
      ]
    })
  }

  return (
    <>
      <div
        className={`button-execute-container button ${rootClassName} `}
        onClick={handleClick}
      >
        <span className="button-execute-text">{ejecutar}</span>
      </div>
      <style jsx>
        {`
          .button-execute-container {
            width: 159px;
            height: 38px;
            display: flex;
            position: relative;
            margin-top: var(--dl-space-space-halfunit);
            align-items: center;
            margin-right: var(--dl-space-space-twounits);
            flex-direction: column;
            justify-content: center;
            background-color: #246fe0;
            cursor: pointer;
          }
          .button-execute-text {
            color: #dee9fb;
          }
        `}
      </style>
    </>
  )
}

ButtonExecute.defaultProps = {
  rootClassName: '',
  ejecutar: 'Iniciar proceso',
  title: 'Confirmar',
  message: '¿Estás seguro de que quieres hacer esto?',
  onYesClick: () => {},
  onNoClick: () => {
    Notify.failure('Operación cancelada')
  }
}

ButtonExecute.propTypes = {
  rootClassName: PropTypes.string,
  ejecutar: PropTypes.string,
  title: PropTypes.string,
  message: PropTypes.string,
  onYesClick: PropTypes.func,
  onNoClick: PropTypes.func
}

export default ButtonExecute
