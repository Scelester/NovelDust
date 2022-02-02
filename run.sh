#!/bin/bash

cd NinedustMainProj
gunicorn Ninedust.wsgi:application