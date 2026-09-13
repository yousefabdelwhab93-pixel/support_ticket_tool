# Nonprofit Support Ticket Tool

A simple AI-powered support ticket classifier for nonprofit teams.

## What does it do?

The tool takes a messy donor email or support request and converts it
into a structured support ticket.

The ticket contains:

- category
- priority
- summary
- next_action

## Project Structure

support_ticket_tool/
│
├── main.py
├── prompts.py
├── examples.py
├── models.py
├── security.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## How it works

Messy Donor Message
        ↓
RFTC System Prompt
        ↓
Few-shot Examples
        ↓
Security Rules
        ↓
Inception Labs API
        ↓
JSON Output
        ↓
Pydantic Validation
        ↓
Support Ticket

## Setup

Install the required packages:

```bash
pip install -r requirements.txt