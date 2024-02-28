# install flask from pip3
package { 'flask':
    ensure =>  'installed',
    install_options =>  ['-v', '2.1.0'],
    provider => 'pip3'
}