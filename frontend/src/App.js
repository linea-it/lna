import React, { Component } from 'react';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import 'typeface-roboto';
import blueGrey from '@material-ui/core/colors/blueGrey';
import pink from '@material-ui/core/colors/pink';

import { Router, Route, Switch } from 'react-router-dom';
import history from './history';
import Home from 'views/Home/'

const theme = createMuiTheme({
  palette: {
    primary: {
      light: '#5c6b7d',
      main: '#34465d',
      dark: '#243141',
      contrastText: '#fff',
    },
    secondary: pink,
  },
  typography: {
    useNextVariants: true,
  },
});

class App extends Component {
  render() {
    return (
      <MuiThemeProvider theme={theme}>
        <Router history={history}>
          <Switch>
            {/* <Route path="/login" name="Login" component={Login} /> */}
            <Route path="/" name="Home" component={Home} />
          </Switch>
        </Router>
      </MuiThemeProvider>
    );
  }
}

export default App;
