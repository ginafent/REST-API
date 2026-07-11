from fastapi import FastAPI, HTTPException
import psycopg2
import psycopg2.extras

app = FastAPI()

DATABASE_URL = "postgresql://appuser:apppassword@localhost:5432/servicedb"


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/services/{service_id}")
def get_service(service_id: int):
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=psycopg2.extras.RealDictCursor)
    cur = conn.cursor()

    # service + customer
    cur.execute(
        """
        SELECT s.serviceID, c.customerID, c.customerFirstName, c.customerLastName
        FROM services s
        JOIN customers c ON c.customerID = s.customerID
        WHERE s.serviceID = %s
        """,
        (service_id,)
    )
    service_row = cur.fetchone()

    if service_row is None:
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail=f"Service {service_id} not found")

    # feedback for that service (could be zero, one, or many rows)
    cur.execute(
        "SELECT feedbackID, comment FROM feedback WHERE serviceID = %s",
        (service_id,)
    )
    feedback_rows = cur.fetchall()

    cur.close()
    conn.close()

    return {
        "serviceID": service_row["serviceid"],
        "customer": {
            "customerID": service_row["customerid"],
            "firstName": service_row["customerfirstname"],
            "lastName": service_row["customerlastname"],
        },
        "feedback": [
            {"feedbackID": f["feedbackid"], "comment": f["comment"]}
            for f in feedback_rows
],
    }