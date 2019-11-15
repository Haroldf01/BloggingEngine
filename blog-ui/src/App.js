// import React from 'react';
// import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

// import HomepageLayout from './Components/Layouts/Homepage';
// import StickyLayout from './Components/Layouts/StickyLayout';
// import Basic from './Components/Typography';

// function App() {
//   return (
//     <Router>
//       <React.Fragment>
//         <Switch>
//           <Route path='/' exact component={HomepageLayout} />
//           <Route path='/blog' component={StickyLayout} />
//           <Route path='/test' component={Basic} />
//         </Switch>
//       </React.Fragment>
//     </Router>
//   );
// }

// export default App;
// App.js
import React, { Component } from 'react';

class App extends Component {
  state = {
    todos: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const todos = await res.json();
      console.log(todos)
      this.setState({
        todos
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
            <br />
            <span>{item.content}</span>
            <br />
            <span>{item.created_on}</span>
            <br />
            <img src={item.img} />
          </div>
        ))}
      </div>
    );
  }
}

export default App;
