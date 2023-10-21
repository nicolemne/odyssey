import Button from 'react-bootstrap/Button';
import './App.module.css';
import styles from './styles/NavBar.module.css';
import NavBar from './components/NavBar';

function App() {
  return (
    <div className={styles.App}>
            <NavBar/>
    </div>
  );
}

export default App;