import React, { PropsWithChildren } from 'react';
import Menu from './components/Menu';
import Nav from './components/Nav';


const Wrapper = (props: PropsWithChildren<any>) => {
    return (
        <div>
            <Nav />

            <div className="container-fluid">
                <div className="row">
                    <Menu />

                    <main role="main" className="col-md-9 ms-sm-auto col-lg-10 px-md-4" id="main">
                        {props.children}
                    </main>
                </div>
            </div>
        </div >
    );
};

export default Wrapper;