import React from 'react'

import AppComponent from './component'
import ButtonExecute from './button-execute'

const CenterBox = (props) => {
  return (
    <>
      <div className="center-box-container">
        <div className="center-box-container1">
          <AppComponent></AppComponent>
        </div>
        <ButtonExecute rootClassName="button-execute-root-class-name"></ButtonExecute>
      </div>
      <style jsx>
        {`
          .center-box-container {
            flex: 0 0 auto;
            width: 562px;
            height: 538px;
            display: flex;
            position: relative;
            align-items: center;
            flex-direction: column;
            justify-content: center;
            background-color: #ffffff;
          }
          .center-box-container1 {
            flex: 0 0 auto;
            width: 428px;
            display: flex;
            align-items: center;
            flex-direction: row;
            justify-content: center;
          }
        `}
      </style>
    </>
  )
}

export default CenterBox
