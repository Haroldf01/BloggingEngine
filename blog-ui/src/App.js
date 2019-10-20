import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import HomepageLayout from './Components/Layouts/Homepage';
import StickyLayout from './Components/Layouts/StickyLayout';
import Basic from './Components/Typography';

function App() {
  return (
    <Router>
      <React.Fragment>
        <Switch>
          <Route path='/' exact component={HomepageLayout} />
          <Route path='/blog' component={StickyLayout} />
          <Route path='/test' component={Basic} />
        </Switch>
      </React.Fragment>
    </Router>
  );
}

export default App;
