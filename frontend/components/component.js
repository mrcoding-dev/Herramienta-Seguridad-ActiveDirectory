import React from 'react'

import PropTypes from 'prop-types'

const AppComponent = (props) => {
  return (
    <>
      <div className="component-container">
        <span>{props.descripcion}</span>
      </div>
      <style jsx>
        {`
          .component-container {
            width: 100%;
            height: 103px;
            display: flex;
            position: relative;
            align-items: center;
            justify-content: center;
          }
        `}
      </style>
    </>
  )
}

AppComponent.defaultProps = {
  descripcion: 'Sistema de ejecución del proceso de cuentas en desuso',
}

AppComponent.propTypes = {
  descripcion: PropTypes.string,
}

export default AppComponent
