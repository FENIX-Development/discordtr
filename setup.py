from distutils.core import setup
setup(
  name = 'discordtr',         
  packages = ['discordtr'],  
  version = '0.7',      
  license='MIT',       
  description = 'developed by fenix-development',  
  author = 'JaimiTR',                  
  author_email = 'jaimitr14@gmail.com',     
  url = 'https://github.com/FENIX-Development/discordtr',  
  download_url = 'https://github.com/FENIX-Development/discordtr/archive/v_07.tar.gz',   
  keywords = ['discordtr', 'fenixdev', 'discord-tr'],  
  install_requires=[           
          'discordtr',
          'komutlar'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
