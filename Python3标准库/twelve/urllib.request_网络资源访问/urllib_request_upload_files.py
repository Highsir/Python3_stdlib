import io
import mimetypes
from urllib import request
import uuid

class MutiPartForm:
    def __init__(self):
        self.form_fields = []
        self.files = []
        self.boundary = uuid.uuid4().hex.encode('utf-8')
        return

    def get_content_type(self):
        return 'multipart/form-data; boundary={}'.format(self.boundary.decode('utf-8'))

    def add_field(self, name, value):
        'add a simple field to the form data'
        self.form_fields.append((name, value))

    def add_file(self, fieldname, filename, fileHandle, mimetype=None):
        "add a file to be upload"
        body = fileHandle.read()
        if mimetype is None:
            mimetype = (
                mimetypes.guess_type(filename)[0] or
                'application/octet-stream'
            )
        self.files.append((fieldname, filename,mimetype, body))
        return
    @staticmethod
    def _form_data(name):
        return ('Content-Disposition: form-data; '
                'name="{}"\r\n').format(name).encode('utf-8')
    @staticmethod
    def _attached_file(name, filename):
        return ('Content-Disposition: file; '
                'name="{}"; filename="{}"\r\n').format(name, filename).encode('utf-8')
    @staticmethod
    def _content_type(ct):
        return 'Content-Type: {}\r\n'.format(ct).encode('utf-8')

    def __bytes__(self):
        "return a byte_string representing the form data, including attached files"
        buffer = io.BytesIO()
        boundary = b'--' + self.boundary + b'\r\n'

        #add the form fields
        for name, value in self.form_fields:
            buffer.write(boundary)
            print(name)
            buffer.write(self._form_data(name))
            buffer.write(b'\r\n')
            buffer.write(value.encode('utf-8'))
            buffer.write(b'\r\n')

        # add the files to upload
        for f_name, filename, f_content_type, body in self.files:
            buffer.write(boundary)
            buffer.write(self._attached_file(f_name, filename))
            buffer.write(self._content_type(f_content_type))
            buffer.write(b'\r\n')
            buffer.write(body)
            buffer.write(b'\r\n')
        buffer.write(b'--' + self.boundary + b'--\r\n')
        return buffer.getvalue()
if __name__ == '__main__':
    "create the form with simple fields."

    form = MutiPartForm()
    form.add_field('firstname', 'Doug')
    form.add_field('lastname','Hellmann')

    # add a fake file
    form.add_file(
        'biography', 'bio.txt', fileHandle=io.BytesIO(b'Pyhton developer and blogger.')
    )
    data = bytes(form)
    r = request.Request('http://localhost:8080/', data=data)
    r.add_header(
        'User-agent',
        'PyMOTW (https://pymotw.com/)',
    )
    r.add_header('Content-type',form.get_content_type())
    r.add_header('Content-length', len(data))
    print()
    print('OUTGOING DATA: ')
    for name, value in r.header_items():
        print('{}: {}'.format(name, value))
    print()
    print(r.data.decode('utf-8'))

    print()
    print('SERVER RESPONSE')
    print(request.urlopen(r).read().decode('utf-8'))