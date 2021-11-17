DATABASES = {
    'aws-db-1': {
        'database': 'Company',
        'user': 'postgres',
        'password': '*******',
        'host': 'hostname.com'
    },
    'localpg': {
        'database': 'Company',
        'user': 'postgres',
        'password': '********',
        'host': 'localhost'
    },
    'extrapg': {
        'database': 'Company',
        'user': 'postgres',
        'password': '********',
        'host': 'azikdev-pg-server.com'
    }
}

use_db = 'aws-db-1'
