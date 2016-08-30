# Get flask
from flask import Flask, request

# Create the app
app = Flask(__name__)

# Load the controller
import restsrv.routes
