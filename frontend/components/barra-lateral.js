import React from 'react';
import PropTypes from 'prop-types';
import { open } from '@tauri-apps/api/shell';

const BarraLateral = (props) => {
  const handleMicrosoftClick = () => {
    open('https://developer.microsoft.com/en-us/graph/graph-explorer');
  };

  return (
    <>
      <div className="barra-lateral-container">
        <div className="barra-lateral-container1"></div>
        <div className="barra-lateral-container2">
          <img
            alt={props.image_alt2}
            src={props.image_src2}
            className="barra-lateral-image"
          />
        </div>
        <button
          onClick={handleMicrosoftClick}
          className="barra-lateral-microsoft-button"
        >
          <img
            alt={props.image_alt1}
            src={props.image_src1}
            className="barra-lateral-image1"
          />
        </button>
      </div>
      <style jsx>
        {`
          .barra-lateral-container {
            flex: 0 0 auto;
            width: 141px;
            height: 1002px;
            display: flex;
            position: relative;
            align-items: flex-start;
            flex-direction: column;
            justify-content: flex-start;
            background-color: #246fe0;
          }
          .barra-lateral-container1 {
            flex: 0 0 auto;
            width: 100%;
            border: 2px dashed rgba(120, 120, 120, 0.4);
            height: 100px;
            display: flex;
            align-items: flex-start;
            flex-direction: column;
          }
          .barra-lateral-container2 {
            width: 100%;
            height: 107px;
            display: flex;
            align-items: center;
            flex-direction: column;
            justify-content: center;
          }
          .barra-lateral-image {
            width: 100px;
            object-fit: cover;
          }
          .barra-lateral-image1 {
            width: 100px;
            object-fit: cover;
          }
          .barra-lateral-microsoft-button {
            background: none;
            border: none;
            cursor: pointer;
          }
          @media (max-width: 991px) {
            .barra-lateral-image {
              width: 50%;
              height: 70px;
            }
            .barra-lateral-image1 {
              left: 36px;
              width: 62px;
              bottom: 95px;
              height: 60px;
              position: absolute;
              padding-top: 0px;
            }
          }
        `}
      </style>
    </>
  );
};

BarraLateral.defaultProps = {
  image_src2: '/playground_assets/userlogo.svg',
  image_alt2: 'image',
  image_src1: '/playground_assets/microsoft%20logo.svg',
  image_alt1: 'image',
};

BarraLateral.propTypes = {
  image_src2: PropTypes.string,
  image_alt2: PropTypes.string,
  image_src1: PropTypes.string,
  image_alt1: PropTypes.string,
};

export default BarraLateral;
