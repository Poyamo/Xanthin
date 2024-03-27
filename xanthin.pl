use strict;
use warnings;
$xanthin = "xanthin";
print($xanthin);
$typePost = ""
  # first, create your message
use Email::MIME;
my $message = Email::MIME->create(
  header_str => [
    From    => 'you@example.com',
    To      => 'friend@example.com',
    Subject => 'Happy birthday!',
  ],
  attributes => {
    encoding => 'quoted-printable',
    charset  => 'ISO-8859-1',
  },
  body_str => "Happy birthday to you!\n",
);

use Email::Sender::Simple qw(sendmail);
sendmail($message);