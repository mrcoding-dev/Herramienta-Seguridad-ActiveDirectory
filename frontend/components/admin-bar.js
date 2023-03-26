import React from 'react';
import PropTypes from 'prop-types';
import TokenButton from './token-button';

const AdminBar = (props) => {
  return (
    <>
      <div className="admin-bar-container">
        <div className="admin-bar-container1">
          <span className="admin-bar-text">{props.admin}</span>
        </div>
        <div className="admin-bar-container2">
          <TokenButton></TokenButton>
        </div>
      </div>
      <style jsx>
        {`
          .admin-bar-container {
            width: 164px;
            height: 1000px;
            display: flex;
            position: relative;
            align-items: center;
            flex-direction: column;
            justify-content: flex-start;
            background-color: #ffffff;
          }
          .admin-bar-container1 {
            flex: 0 0 auto;
            width: 200px;
            height: 100px;
            display: flex;
            align-items: center;
            flex-direction: column;
            justify-content: center;
          }
          .admin-bar-text {
            color: #7f7f82;
          }
          .admin-bar-container2 {
            top: 134px;
            left: 28px;
            width: 109px;
            border: 2px dashed rgba(120, 120, 120, 0.4);
            height: 34px;
            display: flex;
            position: absolute;
            align-items: center;
            flex-direction: column;
            justify-content: center;
            background-color: #fff;
          }
        `}
      </style>
    </>
  );
};

AdminBar.defaultProps = {
  admin: 'Administrador',
};

AdminBar.propTypes = {
  admin: PropTypes.string,
};

export default AdminBar;
