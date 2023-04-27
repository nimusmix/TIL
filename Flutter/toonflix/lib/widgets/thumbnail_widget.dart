import 'package:flutter/material.dart';

class Thumbnail extends StatelessWidget {
  final String url;
  const Thumbnail({
    super.key,
    required this.url,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 250,
      clipBehavior: Clip.hardEdge,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            blurRadius: 20,
            offset: const Offset(4, 4),
            color: Colors.black.withOpacity(0.4),
          ),
        ],
      ),
      child: Image.network(
        url,
        headers: const {
          "User-Agent":
              "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        },
      ),
    );
  }
}
