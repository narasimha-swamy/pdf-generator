function childProcess(filename, Id) {
  const python = require('child_process').spawn('python', ['./resources/app/py/' + filename + '.py', document.getElementById(Id).files[0].path]);
  python.stdout.on('data', function (data) {
    console.log('test: ' + data)
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

function audiobook() {
  const python = require('child_process').spawn('python', ['./resources/app/py/audiobook.py', document.getElementById('speaker-file').files[0].path, document.getElementById('gender').value,
    document.getElementById('rate').value, document.getElementById('volume').value, document.getElementById('start').value
  ]);
  python.stdout.on('data', function (data) {});

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
  });
}

function rearrange() {
  const python = require('child_process').spawn('python', ['./resources/app/py/rearrangepdf.py', document.getElementById('rearrange-file').files[0].path, document.getElementById('outputvalues').value]);
  python.stdout.on('data', function (data) {});
}

function extractpdf(page) {
  const python = require('child_process').spawn('python', ['./resources/app/py/extractpdf.py', document.getElementById('extract-pdf').files[0].path, page]);
  python.stdout.on('data', function (data) {});
}