from flask import Flask
import socket
import time
import os

app = Flask(__name__)
hostname = socket.gethostname()

def calculate_fibonacci(n):
  """Calculates the nth Fibonacci number recursively
  (inefficient for the sake of CPU load)
  """
  if n <= 1:
    return n
  else:
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
    
@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route('/calculate')
def do_calculation():
  start_time = time.time()
  result = calculate_fibonacci(30)  # Adjust the Fibonacci number for load
  end_time = time.time()

  return [{
    'result': result,
    'calculation_time': end_time - start_time,
    'timestamp': start_time,
    'pod_id': hostname
    }]

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)
