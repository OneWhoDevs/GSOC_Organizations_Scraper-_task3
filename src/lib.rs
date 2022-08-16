use pyo3::prelude::*;
use reqwest::StatusCode;


#[pyfunction]
fn request_url(url: &str) -> Py<PyAny> {

    let response = reqwest::blocking::get(url)
        .expect("no proper response from server");

    let req_file = match response.status() {

        StatusCode::OK => response.text().expect("can't turn  response into json file "),
    
        _ => panic!("not OK status from html file"),
        };

    let gil = Python::acquire_gil();
    let py = gil.python();

    req_file.into_py(py)  
    
}

/// A Python module implemented in Rust.
#[pymodule]
fn pyrust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(request_url, m)?)?;
    Ok(())
}


// static APP_USER_AGENT: &str = concat!(env!("CARGO_PKG_NAME","check client.rs"), "/", env!("CARGO_PKG_VERSION","check_client.rs"));

// let client = Client::builder()
// .user_agent(APP_USER_AGENT)
// .build()
// .unwrap();