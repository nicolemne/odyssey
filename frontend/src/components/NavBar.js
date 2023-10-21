import React from 'react';
import styles from '../styles/NavBar.module.css';
import { Navbar, Container, Nav } from "react-bootstrap";
import logo from '../assets/logo.png';

const NavBar = () => {
    return (
        <Navbar className={styles.NavBar} expand="md" fixed="top">
            <Navbar.Brand>
                <img 
                    src={logo} 
                    alt="logo" 
                    height="190" 
                    width="190"
                />
            </Navbar.Brand>
            <Container>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="text-left flex-column">
                        <Nav.Link>
                            <span className={styles.NavItem}>
                                <i className={`fas fa-home ${styles.NavIcon}`}></i>
                                <p>Home</p>
                            </span>
                        </Nav.Link>
                        <Nav.Link>
                            <span className={styles.NavItem}>
                                <i className={`fas fa-sign-in-alt ${styles.NavIcon}`}></i>
                                <p>Sign in</p>
                            </span>
                        </Nav.Link>
                        <Nav.Link>
                            <span className={styles.NavItem}>
                                <i className={`fas fa-user-plus ${styles.NavIcon}`}></i>
                                <p>Sign up</p>
                            </span>
                        </Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}

export default NavBar;
