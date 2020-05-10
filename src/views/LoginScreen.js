import React from 'react'
import Login from '../components/Login'
import PropTypes from 'prop-types'

class Loginscreen extends React.Component {
  constructor (props) {
    super(props)
    this.actions = props.actions
  }
  // we need to replace this, but I suspect with the addition of our new redux usage we want to revamp this a lot anyway
  /* eslint-disable */
  UNSAFE_componentWillMount () {
    var loginmessage = "Not registered yet, Register Now";
    this.setState({
      loginmessage: loginmessage
    })
  }

  static get propTypes () {
    return {
      actions: PropTypes.object,
    }
  }

  render () {
    return (
      <div className="loginscreen">
        <Login/>
        <div>
          {this.state.loginmessage}
        </div>
      </div>
    )
  }
}

export default Loginscreen