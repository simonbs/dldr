class Dldr < Formula
  desc "Download programs from DR TV."
  homepage "https://github.com/simonbs/dldr"
  url "https://github.com/simonbs/dldr/archive/1.0.1.tar.gz"
  version "1.0.1"
  sha256 "8189afca3f1ba83178ae2afe50dc02286dbe43328836f639c30ceb9174f17896"

  depends_on :python3

  resource "docopt" do
    url "https://pypi.python.org/packages/source/d/docopt/docopt-0.6.2.tar.gz"
    sha256 "49b3a825280bd66b3aa83585ef59c4a8c82f2c8a522dbe754a8bc8d08c85c491"
  end

  resource "schema" do
    url "https://pypi.python.org/packages/source/s/schema/schema-0.3.1.tar.gz"
    sha256 "0b9e883edb898971125112f1737d403ffd777513caf69a44b3b0765239797c18"
  end

  resource "requests" do
    url "https://pypi.python.org/packages/source/r/requests/requests-2.9.1.tar.gz"
    sha256 "c577815dd00f1394203fc44eb979724b098f88264a9ef898ee45b8e5e9cf587f"
  end

  def install
    ENV.prepend_create_path "PYTHONPATH", libexec/"vendor/lib/python2.7/site-packages"
    %w[docopt schema requests].each do |r|
      resource(r).stage do
        system "python", *Language::Python.setup_install_args(libexec/"vendor")
      end
    end

    ENV.prepend_create_path "PYTHONPATH", libexec/"lib/python2.7/site-packages"
    system "python", *Language::Python.setup_install_args(libexec)

    bin.install Dir[libexec/"bin/*"]
    bin.env_script_all_files(libexec/"bin", :PYTHONPATH => ENV["PYTHONPATH"])
  end
end
