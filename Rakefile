#!/usr/bin/env rake

# This file benchmarks docdist{1-8}.py on various Python VMs. Running it
# requires Ruby 1.8.7+, Rake, and a checkout of this directory. The benchmark
# results are stored in bench/summary.csv
#
# The implementations are checked for correctness at the same time as they are
# timed, and the Rake process will halt if an error is found.

require 'English'
require 'fileutils'
require 'net/http'
require 'open-uri'

# Python VMs, together with the commands to run them.
vms = [
  ['py27', 'Python 2.7', 'python2.7'],
  ['pypy', 'PyPy 1.5', 'pypy'],
#  ['jython', 'Jython 2.5.2', 'jython']
]

# Fetch the data zip file from the Web.
directory 'bench/input'
file 'bench/input/all.zip' => 'bench/input' do
  open 'http://courses.csail.mit.edu/6.006/fall11/lectures/lecture2_data.zip' do |f|
    File.open 'bench/input/all.zip', 'wb' do |g|
      g.write f.read
    end
  end
end
# Unzip the archive.
inputs = ['bench/input/t2.bobsey.txt', 'bench/input/t3.lewis.txt']
inputs.each do |input|
  file input => 'bench/input/all.zip' do
    Dir.chdir 'bench/input' do
      Kernel.system 'unzip -q all.zip'
    end
    FileUtils.touch input
  end
end
golden_file = 'bench/gold.txt'

# Collect running times.
codes = Dir['*.py'].sort.
    map { |fname| [fname, File.basename(fname).split('.').first] }
codes.each { |code_file, code_name| file code_file }
vms.each do |vm_id, vm_name, vm_cmd|
  codes.each do |code_file, code_name|
    fname = "bench/#{vm_id}-#{code_name}.run"
    file fname => inputs + [code_file, golden_file] do
      print "Running #{code_name} on #{vm_name}... "
      STDOUT.flush
      cmd = "#{vm_cmd} #{code_file} #{inputs.join(' ')}" 
      t0 = Time.now
      out = Kernel.`(cmd)
      t1 = Time.now
      if $CHILD_STATUS.success?
        gold = File.read(golden_file)
        if gold.split("\n")[0, 1].map(&:strip) ==
            out.split("\n")[0, 1].map(&:strip)
          print "OK\n"
          File.open(fname, 'w') { |f| f.write [t1 - t0, "\n", out].join }
        else
          print "incorrect\n"
          print out
          exit 1
        end
      else
        print "failed\n"
        exit 1
      end
    end
    task 'bench/summary.csv' => fname
  end
end

# Output nice spreadsheet.
file 'bench/summary.csv' => 'bench' do
  File.open 'bench/summary.csv', 'w' do |f|
    f.write ','
    f.write codes.map { |code_file, code_name| %Q|"#{code_name}"| }.join(',')
    f.write "\n"
    vms.each do |vm_id, vm_name, vm_cmd|
      f.write %Q|"#{vm_name}"|
      codes.each do |code_file, code_name|
        fname = "bench/#{vm_id}-#{code_name}.run"
        real_time = File.read(fname).strip.to_f
        f.write ",#{real_time}"
      end
      f.write "\n"
    end
  end
end
task :default => 'bench/summary.csv'
