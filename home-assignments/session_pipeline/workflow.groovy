node ('Slave_Static'){

   echo 'Hello World'
   stage('Checkout'){

        dir('Weather') {

            git url: 'https://github.com/L1nuxProdigy/opsschool3-coding'

        }

    }
    sh '''#!/bin/bash

    cd Weather

    python3 /home/ubuntu/jenkins/workspace/Test_freestyle/home-assignments/session2/clickEx.py --city dublin --forecast TODAY+5 -f

    '''

   
}
