#!/bin/sh
set -e

# Install script to install fn

#version=`curl --silent https://api.github.com/repos/ops-micro/cli/releases/latest  | grep tag_name | cut -f 2 -d : | cut -f 2 -d '"'`
version='0.1'
command_exists() {
  command -v "$@" > /dev/null 2>&1
}

case "$(uname -m)" in
  *64)
    ;;
  *)
    echo >&2 'Error: you are not using a 64bit platform.'
    echo >&2 'ops-micro CLI currently only supports 64bit platforms.'
    exit 1
    ;;
esac

user="$(id -un 2>/dev/null || true)"

sh_c='sh -c'
if [ "$user" != 'root' ]; then
  if command_exists sudo; then
    sh_c='sudo -E sh -c'
  elif command_exists su; then
    sh_c='su -c'
  else
    echo >&2 'Error: this installer needs the ability to run commands as root.'
    echo >&2 'We are unable to find either "sudo" or "su" available to make this happen.'
    exit 1
  fi
fi

curl=''
if command_exists curl; then
  curl='curl -sSL -o'
elif command_exists wget; then
  curl='wget -qO'
else
    echo >&2 'Error: this installer needs the ability to run wget or curl.'
    echo >&2 'We are unable to find either "wget" or "curl" available to make this happen.'
    exit 1
fi

#url='https://github.com/veniyer/ops-micro/cli/releases/download'
url='https://raw.githubusercontent.com/veniyer/ops-micro/install/install/install.sh'

# perform some very rudimentary platform detection
case "$(uname)" in
  Linux)
    $sh_c "$curl /tmp/ops-micro_linux $url"
    $sh_c "mv /tmp/ops-micro_linux /usr/local/bin/ops-micro"
    $sh_c "chmod +x /usr/local/bin/ops-micro"
    ops-micro --version
    ;;
  *)
    cat >&2 <<'EOF'

  Either your platform is not easily detectable or is not supported by this
  installer script (yet - PRs welcome! [/install]).
  Please visit the following URL for more detailed installation instructions:

    https://github.com/veniyer/ops-micro

EOF
    exit 1
esac

cat >&2 <<'EOF'


EOF
exit 0