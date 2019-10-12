import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

import HomepageLayout from './Components/Layouts/HomepageLayout';
import StickyLayout from './Components/Layouts/StickyLayout';

function App() {
  return (
    <Router>
      <React.Fragment>
        <Switch>
          <Route path='/' exact component={HomepageLayout} />
          <Route path='/blog' component={StickyLayout} />
        </Switch>
      </React.Fragment>
    </Router>
  );
}

export default App;
