DATABASES = {
    'aws-db-1': {
        'database': 'Company',
        'user': 'postgres',
        'password': '*******',
        'host': 'hostname.com'
    },
    'localpg': {
        'database': 'azikdev',
        'user': 'postgres',
        'password': 'angorelegan2002',
        'host': 'localhost'
    },
    'extrapg': {
        'database': 'Company',
        'user': 'postgres',
        'password': '********',
        'host': 'azikdev-pg-server.com'
    }
}

use_db = 'localpg'
