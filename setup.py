# _*_ coding: mbcs _*_
from distutils.core import setup
import py2exe
import sys, time, re, os

if os.path.exists("comics4pmp.py"):
    os.rename("comics4pmp.py", "comics4pmp.pyw")


if not os.path.exists("version.txt"):   
    buildNum = 0
else:
    buildNum = str(int(open("version.txt", "r").read()) + 1)




# 소스를 수정하여 빌드 넘버를 안에다 삽입 (mainFrame.py)
rex = """# Version:[ ]+([^ \n]+)"""

srcIn = open("mainFrame.py","r")
srcString = srcIn.read()
srcIn.close()

version = re.compile(rex).findall(srcString)[0].split(".")
version[2] = buildNum
newVersion = ".".join(version)

newSrc = re.sub(rex, "# Version:     " + newVersion, srcString, 1)
newSrc = re.sub("version =.+\n", """version = \"%s\"\n""" % newVersion, newSrc, 1)

open("mainFrame.py", "w").write(newSrc)




appName = "comics4PMP"

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "0.2." + buildNum
        self.company_name = "http://www.morcavon.com"
        self.copyright = "morcavon"
        self.name = appName.decode('mbcs')

################################################################
# A program using wxPython

# The manifest will be inserted as resource into test_wx.exe.  This
# gives the controls the Windows XP appearance (if run on XP ;-)
#
# Another option would be to store it in a file named
# test_wx.exe.manifest, and copy it with the data_files option into
# the dist-dir.
#
manifest_template = '''
<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<assembly xmlns='urn:schemas-microsoft-com:asm.v1' manifestVersion='1.0'>
 <trustInfo xmlns="urn:schemas-microsoft-com:asm.v2">
  <security>
   <requestedPrivileges>
    <requestedExecutionLevel level="asInvoker" uiAccess="false"/>
   </requestedPrivileges>
  </security>
 </trustInfo>
</assembly>
'''

RT_MANIFEST = 24

app = Target(
    # used for the versioninfo resource
    description = "jpg 파일을 PMP 화면 크기에 맞게 변환하고 zip으로 압축합니다.".decode('mbcs'),

    # what to build
    script = "%s.pyw" % appName,
##    other_resources = [(RT_MANIFEST, 1, manifest_template)],
    icon_resources = [(1, "icon.ico")],
    )

################################################################

setup(
    options = {"py2exe": {
                          "compressed": 1,
                          "optimize": 2,
                          "dist_dir":appName,
##                          "ascii": 1,
                          "bundle_files": 1,
##                          "packages": "twill",
##                          "includes": "icon",
                          }},
    zipfile = None,
    windows = [app],
##    data_files = ["msvcr90.dll",],
    )


open("version.txt", "w").write(str(buildNum))
