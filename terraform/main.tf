provider "aws" {
  region = "ap-south-1"
}
resource "aws_vpc" "myvpc" {
  cidr_block = "10.0.0.0/16"
}
resource "aws_subnet" "publicsubnet" {
  vpc_id     = aws_vpc.myvpc.id
  cidr_block = "10.0.2.0/24"
}
resource "aws_key_pair" "mykey" {
  key_name   = "Kuber1"
  public_key = file("~/.ssh/id_rsa.pub")
}
resource "aws_instance" "ec2" {
  ami                         = "ami-02b8269d5e85954ef"
  instance_type               = "t3.medium"
  associate_public_ip_address = true
  subnet_id                   = aws_subnet.publicsubnet.id
  root_block_device {
    volume_size = 30    # 30 GB disk
    volume_type = "gp3" # recommended
  }
}