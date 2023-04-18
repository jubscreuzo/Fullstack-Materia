import MinhaPagina from './MinhaPagina';

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/minha-pagina">Minha Página</Link>
            </li>
          </ul>
        </nav>

        <Switch>
          <Route path="/minha-pagina">
            <MinhaPagina />
          </Route>
          <Route path="/">
            <h1>Bem-vindo ao meu aplicativo!</h1>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
