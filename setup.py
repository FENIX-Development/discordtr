from distutils.core import setup
setup(
  name = 'discordtr',         
  packages = ['discordtr'],  
  version = '0.4',      
  license='MIT',       
  description = 'developed by fenix-development',  
  author = 'JaimiTR',                  
  author_email = 'jaimitr14@gmail.com',     
  url = 'https://github.com/FENIX-Development/discordtr',  
  download_url = 'https://github.com/FENIX-Development/discordtr/archive/v_04.tar.gz',   
  keywords = ['discordtr', 'fenixdev', 'discord-tr'],  
  install_requires=[           
          'discordtr',
          'komutlar'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Build Tools',
    'License :: MIT License',
    'Programming Language :: Python :: 3.8',
  ],
)
