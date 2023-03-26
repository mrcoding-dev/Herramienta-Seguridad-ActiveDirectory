import React from 'react'

import PropTypes from 'prop-types'

import CenterBox from './center-box'

const LayorBar = (props) => {
  return (
    <>
      <div className="layor-bar-container">
        <span className="layor-bar-text">{props.desuso}</span>
        <CenterBox></CenterBox>
      </div>
      <style jsx>
        {`
          .layor-bar-container {
            flex: 0 0 auto;
            width: 651px;
            height: 998px;
            display: flex;
            position: relative;
            align-items: center;
            flex-direction: column;
            justify-content: center;
            background-color: #e8eaed;
          }
          .layor-bar-text {
            top: 49px;
            left: 199px;
            color: #747478;
            position: absolute;
          }
        `}
      </style>
    </>
  )
}

LayorBar.defaultProps = {
  desuso: 'Proceso de Cuentas en Desuso',
}

LayorBar.propTypes = {
  desuso: PropTypes.string,
}

export default LayorBar
