CREATE TABLE customers (
    customerID INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,  
    customerFirstName VARCHAR(50) NOT NULL,
    customerLastName VARCHAR(50) NOT NULl
);

CREATE TABLE services (
    serviceID INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,  
    customerID INT NOT NULL,
    FOREIGN KEY (customerID) REFERENCES customers(customerID)
);

CREATE TABLE feedback (
    feedbackID INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    serviceID INT NOT NULL,
    comment VARCHAR(50),

    FOREIGN KEY (serviceID) REFERENCES services(serviceID)
);

INSERT INTO customers (customerFirstName, customerLastName) VALUES
    ('Alice', 'Smith'),
    ('Adam', 'Fenton');

INSERT INTO services (customerID) VALUES
    (1),
    (2);

INSERT INTO feedback (serviceID, comment) VALUES
    (1, 'Good service.'),
    (2, 'Service is rubbish!!');