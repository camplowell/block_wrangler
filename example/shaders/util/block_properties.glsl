#if !defined(BLOCK_ID_MAPPING)
#define BLOCK_ID_MAPPING
// This file was automatically generated by block_wrangler


int emissivity(int id) {
	if (id == 1015) {
		return 1;
	}
	if (id == 1014) {
		return 2;
	}
	if (id == 1013) {
		return 3;
	}
	if (id == 1012) {
		return 4;
	}
	if (id == 1011) {
		return 5;
	}
	if (id == 1010) {
		return 6;
	}
	if (id == 1009) {
		return 7;
	}
	if (id == 1008) {
		return 8;
	}
	if (id == 1007) {
		return 9;
	}
	if (id == 1006) {
		return 10;
	}
	if (id == 1005) {
		return 11;
	}
	if (id == 1004) {
		return 12;
	}
	if (id == 1003) {
		return 13;
	}
	if (id == 1002) {
		return 14;
	}
	if (id == 1000 || id == 1001) {
		return 15;
	}
	return 0;
}


bool sway(int id) {
	return id == 1001 || id == 1020 || id == 1019 || id == 1017 || id == 1018;
}


bool sway_bottom(int id) {
	return id == 1019 || id == 1017;
}


bool crops(int id) {
	return id == 1017 || id == 1018;
}


bool water(int id) {
	return id == 1016;
}


#endif // BLOCK_ID_MAPPING