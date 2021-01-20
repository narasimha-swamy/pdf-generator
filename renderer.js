function converttoocr(){
  console.log(333)
  var python = require('child_process').spawn('python', ['./resources/app/py/ocrconverter.py', document.getElementById('ocr-file').files[0].path]);
  python.stdout.on('data', function (data) {
    console.log('test: ' + data)
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

}
  
function audiobook(){
  var python = require('child_process').spawn('python', ['./resources/app/py/audiobook.py', document.getElementById('speaker-file').files[0].path, document.getElementById('gender').value,
  document.getElementById('rate').value, document.getElementById('volume').value, document.getElementById('start').value]);
  python.stdout.on('data', function (data) {
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}
  
function wordtopdf(){
  var python = require('child_process').spawn('python', ['./resources/app/py/wordtopdf.py', document.getElementById('word-file').files[0].path]);
  console.log(document.getElementById('word-file').files[0].path);
  // console.log('hello');
  python.stdout.on('data', function (data) {
    console.log(data);
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
}

function pdftoword(){
  var python = require('child_process').spawn('python', ['./resources/app/py/pdftoword.py', document.getElementById('Wpdf-file').files[0].path]);
  python.stdout.on('data', function (data) {
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

function exceltopdf(){
  var python = require('child_process').spawn('python', ['./resources/app/py/exceltopdf.py', document.getElementById('excel-file').files[0].path]);
  python.stdout.on('data', function (data) {
  });
}

function pdftoexcel(){
  var python = require('child_process').spawn('python', ['./resources/app/py/pdftoexcel.py', document.getElementById('Edpf-file').files[0].path]);
  python.stdout.on('data', function (data) {
  });
  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });
}

function rearrange() {
  var python = require('child_process').spawn('python', ['./resources/app/py/rearrangepdf.py', document.getElementById('rearrange-file').files[0].path, document.getElementById('outputvalues').value]);
  python.stdout.on('data', function (data) {
  });
}

function extractpdf(page) {
  var python = require('child_process').spawn('python', ['./resources/app/py/extractpdf.py', document.getElementById('extract-pdf').files[0].path, page]);
  python.stdout.on('data', function (data) {
  });
}