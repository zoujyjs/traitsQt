import sipconfig
import os
from PyQt4 import pyqtconfig


def run_sip(sip_config):
	# Generate SIP parameters
	params = sip_params(sip_config)

	# Create build directory if it does not exist
	if not os.path.exists(options.build_path):
		os.makedirs(options.build_path)

	# Execute SIP
	print "%s %s" % (sip_config.sip_bin, " ".join(params))
	os.system("%s %s" % (sip_config.sip_bin, " ".join(params)))

def generate_makefile(sip_config):
	sip_config.default_mod_dir = os.path.join(sip_config.default_mod_dir, 'PyQt4')
	print('Install Module Dir: %s' % (sip_config.default_mod_dir))
	makefile = pyqtconfig.QtGuiModuleMakefile(sip_config, build_file(), dir=options.build_path)
	makefile.extra_include_dirs += [ options.include_path ]
	makefile.extra_lib_dirs += [ options.lib_path ]
	makefile.extra_libs += [ options.lib ]
	makefile.generate()

def sip_params(sip_config):
	params = []

	# Append PyQt SIP flags
	params += [ sip_config.pyqt_sip_flags ]
	# Append PyQt SIP include path
	params += [ "-I", sip_config.pyqt_sip_dir ]
	# Append module search path
	params += [ "-I", os.path.dirname(options.sip_file) ]
	# Append build path
	params += [ "-c", options.build_path ]
	# Append build file
	params += [ "-b", build_file() ]
	# Append main SIP file
	params += [ options.sip_file ]

	return params

def build_file():
	return os.path.join(options.build_path, "%s.sbf" % options.module_name)

def parse_options():
	from optparse import OptionParser

	parser = OptionParser()
	parser.add_option("", "--module-name", dest="module_name", help="the python module name of the lib")
	parser.add_option("", "--sip-file", dest="sip_file", help="the sip file of the lib")
	parser.add_option("", "--lib", dest="lib", help="the name without extension of the lib")
	parser.add_option("", "--lib-path", dest="lib_path", help="the path where the lib dynamic library can be found")
	parser.add_option("", "--include-path", dest="include_path", help="the path where the lib headers can be found")
	parser.add_option("", "--build-path", dest="build_path", help="the path where the Makefile can be found")
	options, args = parser.parse_args()

	return options

options = None

if __name__ == '__main__':
	options = parse_options()

	config = pyqtconfig.Configuration()
	sipconfig.inform("Generating bindings")
	run_sip(config)
	sipconfig.inform("Generating Makefile")
	generate_makefile(config)
	sipconfig.inform("Makefile generated. Run \"nmake\" now.")