from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
import boto3


main_page = Blueprint('main_page', __name__,
                        template_folder='templates')





@main_page.route('/', defaults={'page': 'index'})

@main_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)

@main_page.route('/send', methods=['POST'])
def send():

    firstname = request.form['firstname']
    lastname = request.form['lastname']
    choice = request.form['choice']

    # Create SQS client
    sqs = boto3.client('sqs')

    queue_url = 'https://sqs.eu-west-1.amazonaws.com/ACCOUNTID/myqueue'

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageAttributes={
            'Firstname': {
                'DataType': 'String',
                'StringValue': firstname
            },
            'Lastname': {
                'DataType': 'String',
                'StringValue': lastname
            },
            'Vote': {
                'DataType': 'String',
                'StringValue': choice
            }
        },
        MessageBody=(
            'User {0} {1} has voted for {2}'.format(firstname, lastname, choice)
        )
    )

    return render_template('pages/send.html')
